"""
# Ring Oscillator

Using the inverter delay element defined in `inverter.sch.svg`.
"""

import hdl21 as h
from hdl21.primitives import MosParams
import hdl21schematicimporter as _

# Import the inverter schematic
from .inverter import inverter

# Just in case you don't believe this:
assert isinstance(inverter, h.Generator)


@h.paramclass
class RingOscParams:
    """ Ring Oscillator Parameters """

    mos_params = h.Param(dtype=MosParams, desc="Xtor Params", default=MosParams())


@h.generator
def RingOsc(params: RingOscParams) -> h.Module:
    """ A three-stage ring oscillator """

    @h.module
    class RingOsc:
        VDD, VSS = h.Ports(2)
        a, b, c, = h.Ports(3)

        # Instantiate our 3 schematic inverters
        ia = inverter(params.mos_params)(inp=a, out=b, VDD=VDD, VSS=VSS)
        ib = inverter(params.mos_params)(inp=b, out=c, VDD=VDD, VSS=VSS)
        ic = inverter(params.mos_params)(inp=c, out=a, VDD=VDD, VSS=VSS)

    return RingOsc
