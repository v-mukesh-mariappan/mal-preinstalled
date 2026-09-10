import json
from urllib.request import urlopen


def main():
	"""Make a simple GET request and print the response."""
	with urlopen("https://jsonplaceholder.typicode.com/todos/1", timeout=10) as response:
		data = json.load(response)
	print(data)

	# test


if __name__ == "__main__":
	main()
