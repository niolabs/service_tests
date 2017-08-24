from nio.modules.context import ModuleContext
from nio.util.scheduler.job import Job
from nio.modules.scheduler.module import SchedulerModule

from .scheduler import Scheduler


class TestingSchedulerModule(SchedulerModule):

    def initialize(self, context):
        super().initialize(context)
        # For testing, use a job class that allows us to jump ahead in time
        self.proxy_job_class(Job)

        Scheduler.do_configure(context)
        Scheduler.do_start()

    def finalize(self):
        Scheduler.do_stop()
        super().finalize()

    def prepare_core_context(self):
        context = ModuleContext()
        # set a fine resolution during tests
        context.min_interval = 0.01
        context.resolution = 0.01
        return context
