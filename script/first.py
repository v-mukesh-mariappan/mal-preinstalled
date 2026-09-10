from collections import Counter


def find_unique_char(value: str) -> str | None:
	"""Return the first character that occurs only once, or None."""
	counts = Counter(value)
	return next((char for char in value if counts[char] == 1), None)
