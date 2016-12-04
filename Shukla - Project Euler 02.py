'''Problem 2: Each new term in the Fibonacci sequence is generated by adding the previous two terms. By 
   starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, [...]. By 
   considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of
   the even-valued terms.'''

fiducial_fibonacci_sequence = [0, 1]
for i in xrange(4000000):
    if fiducial_fibonacci_sequence[i] <= 4000000:
        fiducial_fibonacci_sequence.append(fiducial_fibonacci_sequence[i+1]+fiducial_fibonacci_sequence[i])
    else:
        break

'''Note: Building a new list avoids weirdness! If you try to do a loop that lops off the ends of 
   fiducial_fibonacci_sequence, you'll end up with the last element in the list remaining! Python sees 
   "for j in fiducial_fibonacci_sequence", thinks "okay, I have len(fiducial_fibonacci_sequence) elements
   to iterate over", then starts lopping off the relevant terms. However, each lopping off moves the 
   remaining element index up by one, so during the second-to-last iteration, the lopping-off then moves
   the last term up by one. Python then sees itself at len(fibonacci_sequence), since we shortened
   len(fibonacci_sequence), and just assumes it's done.'''

fibonacci_sequence = []
for j in fiducial_fibonacci_sequence:
    if j <= 4000000:
        fibonacci_sequence.append(j)

running_sum = 0
for fibonacci_term in fibonacci_sequence:
    if fibonacci_term % 2 == 0:
        running_sum += fibonacci_term
        
print running_sum