from app.main import is_isogram


def test_to_check_is_word_is_isogram():
    assert is_isogram('playgrounds') is True
    assert is_isogram('look') is False
    assert is_isogram('Adam') is False
    assert is_isogram('') is True
    assert is_isogram('a') is True
    assert is_isogram('ab') is True
    assert is_isogram('aa') is False
