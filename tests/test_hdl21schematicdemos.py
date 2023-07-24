"""
# Hdl21 Schematic Demos 

Unit Tests 
"""

import sys
import hdl21 as h
import sky130_hdl21 as sky130

# DUT Imports
from hdl21schematicdemos import RingOsc, RingOscParams, inverter


def test_serialize_vlsir():
    """Test serializing to VLSIR ProtoBufs"""
    protos = h.to_proto(RingOsc(RingOscParams()))
    print(protos)


def test_compile_inverter():
    """Test compiling the inverter schematic to the `sky130` PDK package."""
    i = inverter()
    sky130.compile(i)
    protos = h.to_proto(i)
    print(protos)


def test_compile_ring():
    """Test compiling the ring generator to the `sky130` PDK package."""
    r = RingOsc(RingOscParams())
    sky130.compile(r)
    protos = h.to_proto(r)
    print(protos)


def test_netlist_inverter():
    """ Test netlisting in various formats """
    r = RingOsc(RingOscParams())

    # Since `sky130` is the sole PDK in memory, `h.pdk.compile` will use it.
    h.pdk.compile(r)

    # And send netlist results to stdout
    h.netlist(r, dest=sys.stdout, fmt="spice")
    h.netlist(r, dest=sys.stdout, fmt="spectre")
    h.netlist(r, dest=sys.stdout, fmt="verilog")
