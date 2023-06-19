import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pytesseract
import PIL.Image
import cv2

myconfig = r"--psm 6 --oem 3"

text1 = pytesseract.image_to_string(PIL.Image.open("sample1.jpg"), config=myconfig)

#print(text)

file = open('file1.txt','w')

file.write(text1)
file.close()

text2 = pytesseract.image_to_string(PIL.Image.open("sample2.jpg"), config=myconfig)

file = open('file2.txt','w')

file.write(text2)
file.close()

text2 = pytesseract.image_to_string(PIL.Image.open("sample3.jpg"), config=myconfig)

file = open('file3.txt','w')

file.write(text2)
file.close()

text2 = pytesseract.image_to_string(PIL.Image.open("sample4.jpg"), config=myconfig)

file = open('file4.txt','w')

file.write(text2)
file.close()

student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]

student_notes = [open(File).read() for File in student_files]

vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()

similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vectors = vectorize(student_notes)

s_vectors = list(zip(student_files, vectors))


def check_plagiarism():
    plagiarism_results = set()
    global s_vectors
    for student_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b , text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            score = (student_pair[0], student_pair[1], sim_score)
            plagiarism_results.add(score)
    return plagiarism_results


for data in check_plagiarism():
        print("file 1 - ", data[0], end =", ")
        print("file 2 - ", data[1], end =" : ")
        print("Degree of similarity = ","%.8f"%data[2])
                                           
