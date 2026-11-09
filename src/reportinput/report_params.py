from typing import List

def gen_params(a, b) -> list[str]:
    """Return unique lowercase words from a that also appear in b."""
    common_words = []
    second_words = [word.lower() for word in b.split()]

    for initial_word in a.split(","):
        normalized_word = initial_word.strip().lower()
        if not normalized_word or normalized_word in common_words:
            continue

        for second_word in second_words:
            if normalized_word == second_word:
                common_words.append(normalized_word)
                break

    return common_words
