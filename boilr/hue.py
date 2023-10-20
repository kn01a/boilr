from huesdk import Hue
import logging
import boilr.config as config

logger = logging.getLogger(__name__)

def switch(state: bool):
    myHue = Hue(bridge_ip=config.HueConfig.ip, username=config.HueConfig.user)
    myDevice = myHue.get_light(name=config.HueConfig.device_name)
    if state:
        myDevice.on()
    else:
        myDevice.off()

    logger.debug("Set HUE Device 'Standleuchte1' to %s", "ON" if state else "OFF")

    return True