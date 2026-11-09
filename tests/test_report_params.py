
from reportinput.report_params import gen_params


def test_gen_params_matches_readme_example():
    first_input = "Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox"
    second_input = "Frog  apple    fox cat fish fish"

    assert gen_params(first_input, second_input) == ["frog", "fish", "apple", "fox"]


def test_gen_params_trims_whitespace_and_removes_duplicates():
    assert gen_params(" Cat, cat , DOG, dog ", "dog cat cat") == ["cat", "dog"]

def test_gen_param_simple_casing():
    assert gen_params("Cat,DOG", "dOg cat") == ["cat", "dog"]

def test_gen_params_matches_whole_tokens_only():
    assert gen_params("catfish,pineapple", "cat fish apple") == []


def test_gen_params_handles_empty_inputs_and_no_matches():
    assert gen_params("", "cat fish") == []
    assert gen_params("cat,fish", "") == []
    assert gen_params("cat", "fish") == []
