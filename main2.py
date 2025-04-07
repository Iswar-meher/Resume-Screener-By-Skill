import pandas as pd
import re

# -------------------- Helper Functions -------------------- #
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def search_resumes_by_skill(resume_list, skill):
    skill = skill.lower().strip()
    matched_resumes = []

    for idx, resume in enumerate(resume_list):
        if skill in clean_text(resume):
            matched_resumes.append((idx + 1, resume.strip()))

    return matched_resumes

# -------------------- Resume Input -------------------- #
resumes = [
    """
    Experienced software engineer with 5 years in Python and Django.
    Built scalable APIs and deployed applications on AWS.
    """,
    """
    Web developer with solid knowledge of React, JavaScript, and Bootstrap.
    Contributed to frontend design and component-based architecture.
    """,
    """
    Data analyst proficient in SQL, Tableau, and data storytelling.
    Looking to transition into data science.
    """
]

# -------------------- User Skill Input -------------------- #
skill_to_search = input("🔍 Enter the skill you want to search for: ")

# -------------------- Search Logic -------------------- #
results = search_resumes_by_skill(resumes, skill_to_search)

# -------------------- Output -------------------- #
print("\n" + "=" * 60)
print(f"🔎 Resumes Matching Skill: {skill_to_search}")
print("=" * 60)

if results:
    for idx, res in results:
        print(f"\n📄 Resume #{idx}")
        print("-" * 40)
        print(res[:500] + ('...' if len(res) > 500 else ''))
else:
    print("❌ No resumes found with that skill.")

