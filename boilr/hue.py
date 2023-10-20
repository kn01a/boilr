from huesdk import Hue
import logging

logger = logging.getLogger(__name__)

def switch(state: bool):
    myHue = Hue(bridge_ip="192.168.0.107", username="bjjskn0JYFlazBVGbz6ObqhMWiqbZmJvkZ0aJYdQ")
    myDevice = myHue.get_light(name="Standleuchte1")
    if state:
        myDevice.on()
    else:
        myDevice.off()

    logger.debug("Set HUE Device 'Standleuchte1' to %s", "ON" if state else "OFF")

    return True