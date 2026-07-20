print("LEARNER INTERVENTION TRACKER")

name = input("Enter learner's name: ")

dna = int(input("Enter DNA mark: "))
meiosis = int(input("Enter Meiosis mark: "))
vertebrates = int(input("Enter Reproduction in Vertebrates mark: "))
human_reproduction = int(input("Enter Human Reproduction mark: "))
genetics = int(input("Enter Genetics mark: "))

print("\n" + "=" * 40)
print("===== INTERVENTION REPORT")
print("=" * 40)

print(f"\nLearner: {name}")

print("\nTopics requiring intervention:")

intervention_needed = False

if dna < 40:
    print("- DNA: The Code of Life")
    intervention_needed = True

if meiosis < 40:
    print("- Meiosis")
    intervention_needed = True

if vertebrates < 40:
    print("- Reproduction in Vertebrates")
    intervention_needed = True

if human_reproduction < 40:
    print("- Human Reproduction")
    intervention_needed = True

if genetics < 40:
    print("- Genetics")
    intervention_needed = True

if not intervention_needed:
    print("No intervention required.")

lowest_mark = min(
    dna,
    meiosis,
    vertebrates,
    human_reproduction,
    genetics
)

print("\nPriority intervention topic(s):")

if dna == lowest_mark:
    print(f"- DNA: The Code of Life ({dna}%)")

if meiosis == lowest_mark:
    print(f"- Meiosis ({meiosis}%)")

if vertebrates == lowest_mark:
    print(f"- Reproduction in Vertebrates ({vertebrates}%)")

if human_reproduction == lowest_mark:
    print(f"- Human Reproduction ({human_reproduction}%)")

if genetics == lowest_mark:
    print(f"- Genetics ({genetics}%)")
