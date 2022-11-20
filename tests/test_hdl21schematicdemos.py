
import hdl21 as h

# DUT Imports
from hdl21schematicdemos import RingOsc, RingOscParams


def test_serialize_vlsir():
    """ Test serializing to VLSIR ProtoBufs """
    protos = h.to_proto(RingOsc(RingOscParams()))
    print(protos)

