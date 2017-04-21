import os
import re

from otcclient.core.userconfigaction import userconfigaction
from otcclient.core.configloader import configloader
from otcclient.core.OtcConfig import OtcConfig
from otcclient.plugins.ecs import ecs

class TestOtcConfig:
    def setup(self):
        self.save_otc_user_file()
        self.purge_os_env()

    def teardown(self):
        self.restore_otc_user_file() 
        self.restore_os_env()
    
    def purge_os_env(self):
        """Remove OS_* from environment"""
        self._os_env = {k: v for k, v in os.environ.iteritems() if re.match(r'OS_', k)}
        for k in self._os_env:
            del os.environ[k]
    
    def restore_os_env(self):
        """Restore OS_*"""
        os.environ.update(self._os_env) 

    def save_otc_user_file(self):
        self._otc_user_file = OtcConfig.OTC_USER_FILE
        
    def restore_otc_user_file(self):
        OtcConfig.OTC_USER_FILE = self._otc_user_file
        configloader.readUserValues() 

    def test_uservalues(self):
        """Test reading OTC_USER_FILE"""
        OtcConfig.OTC_USER_FILE = "otc_config_mock"
        configloader.readUserValues()
        assert OtcConfig.ak == 'mock_access_key_id'
        assert OtcConfig.sk == 'mock_secret_access_key'
        assert OtcConfig.USERNAME == 'MOCK OTC USER NAME'
        assert OtcConfig.PASSWORD == 'MOCK_API_KEY'
    
# vim: sts=4 ts=4 sw=4 et:
