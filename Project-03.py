from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

roles = {
    "Data Scientist": ["Python", "SQL", "Machine Learning", "Data Analysis", "Statistics"],
    "DevOps Engineer": ["AWS", "Docker", "Kubernetes", "CI/CD", "Automation", "Linux"],
    "Backend Developer": ["Java", "Python", "SQL", "APIs", "Databases"],
    "Frontend Developer": ["JavaScript", "React", "HTML", "CSS", "UI Design"],
    "Cloud Architect": ["AWS", "Cloud Computing", "Networking", "Security", "Automation"],
    "Data Engineer": ["Python", "SQL", "ETL", "Data Pipelines", "Big Data"],
    "Machine Learning Engineer": ["Python", "Machine Learning", "TensorFlow", "Deep Learning", "Data Analysis"],
    "System Administrator": ["Linux", "Networking", "Automation", "Security", "Scripting"],
}

role_names = list(roles.keys())
corpus = [" ".join(skill.lower().replace(" ", "_") for skill in skills) for skills in roles.values()]

skill1 = input("Enter skill 1: ")
skill2 = input("Enter skill 2: ")
skill3 = input("Enter skill 3: ")

user_skills = [skill1, skill2, skill3]
user_doc = " ".join(skill.lower().strip().replace(" ", "_") for skill in user_skills)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus + [user_doc])

user_vector = tfidf_matrix[-1]
role_vectors = tfidf_matrix[:-1]

similarities = cosine_similarity(user_vector, role_vectors)[0]
ranked = sorted(zip(role_names, similarities), key=lambda x: x[1], reverse=True)

print("\nTop 3 Recommended Career Paths:")
for role, score in ranked[:3]:
    print(f"{role} - {round(score * 100, 2)}% match")