"""
Salt state module
"""
import logging

log = logging.getLogger(__name__)

__virtualname__ = "github_runner"


def __virtual__():
    # To force a module not to load return something like:
    #   return (False, "The github_runner state module is not implemented yet")

    # Replace this with your own logic
    if "github_runner.example_function" not in __salt__:
        return False, "The 'github_runner' execution module is not available"
    return __virtualname__


def exampled(name):
    """
    This example function should be replaced
    """
    ret = {"name": name, "changes": {}, "result": False, "comment": ""}
    value = __salt__["github_runner.example_function"](name)
    if value == name:
        ret["result"] = True
        ret["comment"] = "The 'github_runner.example_function' returned: '{}'".format(value)
    return ret
