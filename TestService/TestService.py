import win32service
import win32serviceutil
import win32event
import logging

class TestService(win32serviceutil.ServiceFramework):

    _svc_name_ = "Test Service"

    _svc_display_name_ = "Test Service"

    _svc_description_ = "Service Test"

    _timeout_Milliseconds = 1 * 1000

    def __init__(self, args):

        win32serviceutil.ServiceFramework.__init__(self, args)

        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):

        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)

        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):

        servicemanager.LogMsg(

            servicemanager.EVENTLOG_INFORMATION_TYPE,

            servicemanager.PYS_SERVICE_STARTED,

            (self._svc_name_, '')

        )

if __name__ == '__main__':

    win32serviceutil.HandleCommandLine(TestService)