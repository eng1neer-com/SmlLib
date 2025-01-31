from typing import Optional

from smllib.sml import SmlBaseObj, SmlObjFieldInfo

from .sml_time import build_time, TIME_HINT


class SmlOpenResponse(SmlBaseObj):
    __sml__ = {
        'ref_time': SmlObjFieldInfo(func=build_time)
    }

    codepage: Optional[str]
    client_id: Optional[str]
    req_file_id: str
    server_id: str
    ref_time: TIME_HINT
    sml_version: Optional[int]


class SmlCloseResponse(SmlBaseObj):
    __sml__ = {}

    global_signature: Optional[str]
