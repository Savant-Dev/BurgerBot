'''

    This file handles application-wide configuration

    Available Methods:
        - get (return a value from YAML)
        - fetch (return a value from ENV)
        - request (return a value from API)

    Definitions:
        - YAML Meta-Classes
            Loads data from YAML files into Classes
            Allows for easy data retrieval across the app
            Used via imports

        - Environment Caching
            Used for requesting tokens and other sensitive data
            Only accessible with Developer Secret

        - API Configuration
            Utilizes network-based requests
            Retrieves application settings such as prefix, etc
            Requires Network Access and API Secret            

'''
