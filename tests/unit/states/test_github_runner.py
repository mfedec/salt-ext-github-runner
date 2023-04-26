import pytest
import salt.modules.test as testmod
import saltext.github_runner.modules.github_runner_mod as github_runner_module
import saltext.github_runner.states.github_runner_mod as github_runner_state


@pytest.fixture
def configure_loader_modules():
    return {
        github_runner_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        github_runner_state: {
            "__salt__": {
                "github_runner.example_function": github_runner_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": f"The 'github_runner.example_function' returned: '{echo_str}'",
    }
    assert github_runner_state.exampled(echo_str) == expected
