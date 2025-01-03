data = [
    ("Sujal", 85),
    ("Ansh", 90),
    ("Om", 78),
    ("Dev", 88),
    ("Ved", 92)
]

def analyze_data(data):
    total_score = sum(score for _, score in data)
    count = len(data)
    average_score = total_score / count if count > 0 else 0
    return average_score

def generate_report(data, average_score):
    print("Student Scores Report")
    print("----------------------")
    print("Name       | Score")
    print("----------------------")
    
    for name, score in data:
        print(f"{name:<10} | {score}")
    
    print("----------------------")
    print(f"Average Score: {average_score:.2f}")

def main():
    average_score = analyze_data(data)
    generate_report(data, average_score)

if __name__ == "__main__":
    main()
