import sys
from websshauto._version import __version__, __version_info__


__author__ = 'Scott John <scott@thejohnweb.com>'

if sys.platform == 'win32' and sys.version_info.major == 1 and \
        sys.version_info.minor >= 1:
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
