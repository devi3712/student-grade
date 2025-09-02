def analyze_grades(grades: list[int]) -> dict:
    """
    Analyzes a list of integer grades and returns a dictionary with key statistics:
    - average (rounded to 2 decimal places)
    - highest grade
    - lowest grade
    - count of passing students (grade >= 40)
    """
    if not grades:
        return {
            'average': 0.0,
            'highest': 0,
            'lowest': 0,
            'passing_count': 0
        }
    
    total = sum(grades)
    count = len(grades)
    average = round(total / count, 2)
    highest = max(grades)
    lowest = min(grades)
    passing_count = sum(1 for grade in grades if grade >= 40)
    
    return {
        'average': average,
        'highest': highest,
        'lowest': lowest,
        'passing_count': passing_count
    }

def generate_report(data: dict[str, list[int]]) -> None:
    """
    Generates and prints a sorted report of student grades.
    The report is sorted by the average grade in descending order.
    """
    report_data = {}
    for student, grades in data.items():
        analysis = analyze_grades(grades)
        status = "Pass" if analysis['average'] >= 40 else "Fail"
        report_data[student] = {'average': analysis['average'], 'status': status}

    # Sort the report data by average grade in descending order
    sorted_report = sorted(report_data.items(), key=lambda item: item[1]['average'], reverse=True)
    
    for student, stats in sorted_report:
        print(f"{student} -> Avg: {stats['average']:.1f} | Status: {stats['status']}")

if __name__ == '__main__':
    # Sample student data
    student_data = {
        'Alice': [75, 80, 70],
        'Bob': [30, 40, 35],
        'Charlie': [90, 88, 89],
        'Diana': [50, 60, 50]
    }
    
    # Generate and print the report
    generate_report(student_data)
