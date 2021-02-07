'''
I Love Lance & Janice
=====================

You’ve caught two of your fellow minions passing coded notes back and forth – while they’re on duty, no less! Worse, you’re pretty sure it’s not job-related – they’re both huge fans of the space soap opera “Lance & Janice”. You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting her time passing non-job-related notes, it’ll put you that much closer to a promotion.

Fortunately for you, the minions aren’t exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched. That is, ‘a’ becomes ‘z’, ‘b’ becomes ‘y’, ‘c’ becomes ‘x’, etc. For instance, the word “vmxibkgrlm”, when decoded, would become “encryption”.

Write a function called answer(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about “Lance & Janice” instead of doing their jobs.

Test cases
==========

Inputs:
(string) s = “wrw blf hvv ozhg mrtsg’h vkrhlwv?”
Output:
(string) “did you see last night’s episode?”

Inputs:
(string) s = “Yvzs! I xzm’g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!”
Output:
(string) “Yeah! I can’t believe Lance lost his job at the colony!!”
'''

def solution(x="Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded_message = ""
    for i in range(0, len(x)):
        if x[i] in alphabet:
            index_in_alphabet = alphabet.index(x[i]) # x[0]
            decoded_message = decoded_message + alphabet[25 - index_in_alphabet]
        else:
            decoded_message = decoded_message + x[i]        
    print(decoded_message)

solution()