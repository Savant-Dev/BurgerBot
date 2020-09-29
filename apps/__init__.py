'''

    This file controls the application

    Available Methods:
        - start (begins logging and attempts `connect()`)
        - debug (starts app in subprocess and logs resource usage)

    Definitions:
        - BootLoader
            Establishes Event Logging
            Attempts to Establish API Connection
            Attempts to Start Discord Application

        - Debugger
            Establishes Trace Event Logging
            Attempts to run BootLoader in a Process
            Monitors System Utilization Data for Process

'''
