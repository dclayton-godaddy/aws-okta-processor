"""The token_operations command."""

from __future__ import print_function

from .base import Base
from aws_okta_processor.core.fetcher import ClientInput


class Create(Base):
    """
    Usage:
      create --organization=<okta_organization> --user=<user_name> --name=<profile_name>
             [--pass=<user_pass>]
             [--duration=<duration_seconds>]
             [--silent]

    Options:
      -u <user_name> --user=<user_name>                          Okta user name.
      -p <user_pass> --pass=<user_pass>                          Okta user password.
      -o <okta_organization> --organization=<okta_organization>  Okta organization domain.
      -d <duration_seconds> --duration=<duration_seconds>        Duration of role session [default: 3600].
      -n <profile_name> --name=<profile_name>                    Name to store profile under.
      -s --silent                                                Run silently.
    """  # noqa

    def execute(self):
        client_input = ClientInput(self)



    def get_pass(self):
        if self.args["AWS_OKTA_PASS"]:
            return self.args["AWS_OKTA_PASS"]
