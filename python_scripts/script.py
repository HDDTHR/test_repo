import os
import random
import json
from faker import Faker

fake = Faker()

# Create a directory to store the generated Markdown files
output_dir = "../content/person/"
os.makedirs(output_dir, exist_ok=True)

# Function to generate random data and create a Markdown file
def generate_markdown_file():
    slug = fake.uuid4()
    data = {
        "fullname_en": fake.name(),
        "fullname_ar": fake.name(),
        "age": random.randint(1, 99),
        "gender": random.choice(["Male", "Female"]),
        "dod": fake.date_time_this_decade().isoformat() + "Z",
        "picture": "/img/missing.png",
        "description_en": fake.text(),
        "description_ar": fake.text(),
    }

    # Save the Markdown file
    file_path = os.path.join(output_dir, f"{slug}.json")
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)

# Generate 10,000 Markdown files
for i in range(1, 20000):
    generate_markdown_file()

print("json files generated successfully.")
