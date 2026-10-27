from leap_year import is_leap_year

def test_ordinary_year_is_not_leap():
    assert is_leap_year(2023) is False

def test_divisible_by_4_is_leap():
    assert is_leap_year(2024) is True