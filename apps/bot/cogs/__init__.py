'''

    This file controls Bot Extensions

    Available Methods:
        - get (returns the code currently running in a cog)
        - load (adds a cog to the application; hotloading)
        - unload (removes a cog from the application)
        - reload (refreshes a cog; hot-reloading)

        - update (attempts to push an update to the cog's code)

    Definitions:
        - ExtensionHandler
            Cog Management Interface
            Loads, unloads, and reloads Extension Files
            Uses GitHub commands to push changes without restarting

'''
