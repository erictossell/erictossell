import json
import random
import re


def update_readme(interests_file, readme_file):
    with open(interests_file, "r") as file:
        interests = json.load(file)

    random_interest = random.choice(interests)

    with open(readme_file, "r") as file:
        content = file.read()

    new_content = re.sub(
        r"computing, and (.+?)\.", f"computing, and {random_interest}.", content
    )

    with open(readme_file, "w") as file:
        file.write(new_content)


if __name__ == "__main__":
    update_readme("interests.json", "README.md")
