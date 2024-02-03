from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

def evaluate_translations(reference, candidate):
    smoothing = SmoothingFunction().method1  # Choose a smoothing method
    bleu_score = sentence_bleu([reference.split()], candidate.split(), smoothing_function=smoothing)
    return bleu_score

# Sample data
source_sentences = [
  "I am studying in Institute of Aeronautical Engineering"
]  
google_translations = [
   "J'étudie à l'Institut d'ingénierie aéronautique"
] 
your_translations = [
 "J'étudie à l'Institut de génie aéronautique"
]  

# Evaluation
for source, google_translation, your_translation in zip(source_sentences, google_translations, your_translations):
    bleu_google = evaluate_translations(reference=source, candidate=google_translation)
    bleu_yours = evaluate_translations(reference=source, candidate=your_translation)
    
    improvement_percentage = ((bleu_yours - bleu_google) / bleu_google) * 100 if bleu_google != 0 else 0
    
    print("Source:", source)
    print("Google Translate:", google_translation)
    print("Your Translation:", your_translation)
    print("BLEU Score - Google Translate:", bleu_google)
    print("BLEU Score - Your Translation:", bleu_yours)
    print("Improvement Percentage:", improvement_percentage, "%")
    print()
