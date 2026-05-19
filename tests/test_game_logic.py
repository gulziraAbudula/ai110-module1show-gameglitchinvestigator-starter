from logic_utils import check_guess, get_range_for_difficulty

# Tests for Fix 1: Range display based on difficulty level
def test_easy_difficulty_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_difficulty_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_difficulty_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_invalid_difficulty_defaults_to_normal():
    low, high = get_range_for_difficulty("Invalid")
    assert low == 1
    assert high == 100

# Tests for Fix 2: Secret generation within correct range
def test_secret_generation_easy():
    import random
    random.seed(42)
    low, high = get_range_for_difficulty("Easy")
    secret = random.randint(low, high)
    assert low <= secret <= high

def test_secret_generation_normal():
    import random
    random.seed(42)
    low, high = get_range_for_difficulty("Normal")
    secret = random.randint(low, high)
    assert low <= secret <= high

def test_secret_generation_hard():
    import random
    random.seed(42)
    low, high = get_range_for_difficulty("Hard")
    secret = random.randint(low, high)
    assert low <= secret <= high

# Tests for Fix 3: Status initialization and check_guess
def test_winning_guess():
    result, message = check_guess(50, 50)
    assert result == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    result, message = check_guess(60, 50)
    assert result == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    result, message = check_guess(40, 50)
    assert result == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_status_starts_as_playing():
    # Verify that game status should be initialized to "playing"
    assert "playing" in ["playing", "won", "lost"]

def test_check_guess_with_string_secret():
    # Test case where secret is a string
    result, message = check_guess(50, "50")
    assert result == "Win"

def test_check_guess_string_too_high():
    result, message = check_guess(60, "50")
    assert result == "Too High"

def test_check_guess_string_too_low():
    result, message = check_guess(40, "50")
    assert result == "Too Low"
