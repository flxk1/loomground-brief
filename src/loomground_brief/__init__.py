# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 flxk1
"""loomground-brief — What is the minimum a supervisor must read?

One narrow problem. See :mod:`loomground_brief.brief` for the reasoning;
this module only re-exports it and the version.
"""

from ._version import __version__
from .brief import (
    BriefItem,
    OversightBrief,
    oversight_brief,
    KIND_ORDER,
)

__all__ = [
    "__version__",
    "BriefItem",
    "OversightBrief",
    "oversight_brief",
    "KIND_ORDER",
]
