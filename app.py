def predict(numbers):
    
  
    avg = sum(numbers) / len(numbers)
    if avg > 50:
        return "High"
    else:
        return "Low"


if __name__ == "__main__":
    sample = [10, 20, 30, 40, 100]
    print("Input:", sample)
    print("Prediction:", predict(sample))