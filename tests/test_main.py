import pytest

def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

def test_lcs():
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("abcdef", "zbcdfg") == 4
    assert longest_common_subsequence("", "abc") == 0
    assert longest_common_subsequence("abc", "") == 0
    assert longest_common_subsequence("", "") == 0

def test_lcs_equal_strings():
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abcdef", "abcdef") == 6

def test_lcs_repeated_chars():
    assert longest_common_subsequence("aaaa", "aaaa") == 4
    assert longest_common_subsequence("abcabc", "abcabc") == 6
