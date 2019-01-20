name = data.get('name', 'world')
logger.fatal("Hello {}".format(name))
hass.bus.fire(name, { "wow": "from a Python script!" })
