Image Compression using SVD:

This is my Matrix Theory project where I implemented image compression using the Singular Value Decomposition (SVD) method in Python.

Project Overview:

An image can be thought of as a big matrix made up of numbers (pixel values).
Using SVD, this matrix can be broken into three parts:
A = U Σ Vᵀ
Here:
U and V contain information about the structure of the image
Σ (Sigma) contains values that represent the strength or importance of those structures
If we take only the top k singular values, we can rebuild an approximate version of the image.
This helps reduce the size of the image while keeping it visually almost the same.
That is basically what image compression is.
The project also calculates the Frobenius norm error, which shows how close the reconstructed image is to the original.

Features:

Calculates SVD manually 

Uses:

Power Iteration method for finding eigenvalues
Gram-Schmidt process to make vectors orthogonal
Deflation to find multiple eigenvectors
Reconstructs and displays the image using top k singular values
Prints the reconstruction error in the terminal
How It Works:
The image is read and converted into a grayscale matrix A
Compute B = Aᵀ × A
Use the Power Iteration method to find the top k eigenvalues and eigenvectors of B
Calculate singular values using σ = √λ
Compute U = (A × V) / σ
Rebuild the image using only top k singular values
Show the final compressed image
The difference between the original and reconstructed image is measured using the Frobenius norm.

How to Run:

Open the project folder in any code editor like termmux
Run the code using the command:
python svd_compression.py
Enter the image file name (example: einstein.jpg)
Enter the value of k (example: 100)
The program will show the compressed image and also print the error value in the terminal.
when k increases, the error decreases and the image looks clearer.
Observations:

Smaller k gives more compression but poor image quality
Larger k gives better image quality but less compression
For most images, k between 50 and 100 gives good results
The Frobenius error helps measure how accurate the reconstruction is