from github_actions_test.module1 import fun

a = 5

g: int = "fo"


def test_fun():
    assert fun(4) == 8
