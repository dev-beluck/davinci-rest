# this script must be placed in the davinci resolve script folder

from davinci_rest.server import launch

launch(resolve, port=5001) # type: ignore
