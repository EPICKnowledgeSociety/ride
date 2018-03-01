from firedex_algorithm import FiredexAlgorithm

import logging
log = logging.getLogger(__name__)


class NullFiredexAlgorithm(FiredexAlgorithm):
    """
    Algorithm implementation that assigns priorites randomly for a baseline comparison with actual algorithms.
    """

    def __init__(self, **kwargs):
        super(NullFiredexAlgorithm, self).__init__(**kwargs)

    def _run_algorithm(self, configuration):
        flow = configuration.net_flows[0]
        prio = configuration.prio_classes[0]
        for t in configuration.topics:
            self.set_topic_net_flow(t, flow)
        for f in configuration.net_flows:
            self.set_net_flow_priority(f, prio)