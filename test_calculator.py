from leap_year import is_leap_year

def test_ordinary_year_is_not_leap():
    assert is_leap_year(2023) is False