def calculate_metrics(TP, TN, FP, FN):
    total = TP + TN + FP + FN
    accuracy = (TP + TN) / total if total else 0

    precision = TP / (TP + FP) if (TP + FP) else 0
    recall = TP / (TP + FN) if (TP + FN) else 0
    specificity = TN / (TN + FP) if (TN + FP) else 0
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0

    return {
        "Accuracy": round(accuracy, 4),
        "Precision": round(precision, 4),
        "Recall": round(recall, 4),
        "Specificity": round(specificity, 4),
        "F1-Score": round(f1_score, 4)
    }

# Example arbitrary values
TP = 70  # True Positives
TN = 50  # True Negatives
FP = 10  # False Positives
FN = 20  # False Negatives

# Calculate metrics
results = calculate_metrics(TP, TN, FP, FN)

# Print the results
for metric, value in results.items():
    print(f"{metric}: {value}")
