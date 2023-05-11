import pytest  # used for our unit tests


def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    if hours > 0:
        return f"{hours}h{minutes}min{seconds}s"
    elif minutes > 0:
        return f"{minutes}min{seconds}s"
    else:
        return f"{seconds}s"


#Below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator.
#The first element in the tuple is the name of the test case, and the second element is the argument passed to the format_time function.
@pytest.mark.parametrize("test_input,expected", [
    ("positive integer", (3600, "1h0min0s")),
    ("negative integer", (-3600, "-1h0min0s")),
    ("zero", (0, "0s")),
])
def test_format_time_normal(test_input, expected):
    # This test verifies that the format_time function returns the expected string when passed a positive integer, negative integer, or zero.
    result = format_time(expected[0])
    assert result == expected[1]


#Below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator.
#The first element in the tuple is the name of the test case, and the second element is the argument passed to the format_time function.
@pytest.mark.parametrize("test_input,expected", [
    ("non-integer", ValueError),
    ("string", ValueError),
    ("list", ValueError),
    ("dictionary", ValueError),
    ("tuple", ValueError),
    ("set", ValueError),
    ("float", ValueError),
    ("None", ValueError),
])
def test_format_time_edge(test_input, expected):
    # This test verifies that the format_time function raises the expected ValueError when passed a non-integer value, string, list, dictionary, tuple, set, float, or None.
    with pytest.raises(expected):
        format_time(test_input)