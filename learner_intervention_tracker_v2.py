import csv


def calculate_risk_level(average):
    if average < 40:
        return "High Risk"
    elif average < 50:
        return "Moderate Risk"
    else:
        return "Low Risk"


def find_intervention_topics(topics):
    intervention_topics = []

    for topic, mark in topics.items():
        if mark < 40:
            intervention_topics.append(topic)

    return intervention_topics


print("LEARNER INTERVENTION REPORT")
print("=" * 40)

topic_interventions = {
    "DNA": 0,
    "Meiosis": 0,
    "Reproduction in Vertebrates": 0,
    "Human Reproduction": 0,
    "Genetics": 0
}

total_learners = 0
learners_requiring_intervention = 0

highest_average = 0
top_learner = ""

with open("learner_marks.csv", "r") as file:
    reader = csv.DictReader(file)

    for learner in reader:

        total_learners += 1

        name = learner["name"]

        topics = {
            "DNA": int(learner["dna"]),
            "Meiosis": int(learner["meiosis"]),
            "Reproduction in Vertebrates": int(learner["vertebrates"]),
            "Human Reproduction": int(learner["human_reproduction"]),
            "Genetics": int(learner["genetics"])
        }

        average = sum(topics.values()) / len(topics)

        risk_level = calculate_risk_level(average)

        if average > highest_average:
            highest_average = average
            top_learner = name

        intervention_topics = find_intervention_topics(topics)

        for topic in intervention_topics:
            topic_interventions[topic] += 1

        if intervention_topics:

            learners_requiring_intervention += 1

            print("\n" + "=" * 40)
            print(f"Learner: {name}")
            print(f"Average: {average:.1f}%")
            print(f"Risk Level: {risk_level}")

            print("\nTopics requiring intervention:")

            for topic in intervention_topics:
                print(f"- {topic}")

print("\n" + "=" * 40)
print("CLASS INTERVENTION SUMMARY")
print("=" * 40)

for topic, count in topic_interventions.items():
    print(f"{topic}: {count} learners require intervention")

most_challenging_topic = max(
    topic_interventions,
    key=topic_interventions.get
)

print("\nMost Challenging Topic:")
print(
    f"{most_challenging_topic} "
    f"({topic_interventions[most_challenging_topic]} learners require intervention)"
)

print("\n" + "=" * 40)
print("OVERALL CLASS STATISTICS")
print("=" * 40)

print(f"Total Learners: {total_learners}")
print(f"Learners Requiring Intervention: {learners_requiring_intervention}")

print("\nTOP PERFORMING LEARNER")
print("=" * 40)
print(f"Learner: {top_learner}")
print(f"Average: {highest_average:.1f}%")