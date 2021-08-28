import argparse
from talked.main import app


def setup_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="""The hostname or ip the internal server should bind to.
        If the value is a path that starts with unix:// the internal server
        will bind to a unix socket instead of a TCP socket.""",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help="The port the internal server should bind to.",
    )
    return parser


parser = setup_arguments()
args = parser.parse_args()
app.run(host=args.host, port=args.port, threaded=False)
