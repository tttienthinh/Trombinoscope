
import os
liste = os.listdir('Photo/')
liste.sort()

import sys
sys.stdout = open('Latex.tex', 'w')

print("\\documentclass[a4paper, 11pt]{article}")
print("\\usepackage{caption}")
print("\\usepackage{subcaption}")
print("\\usepackage{graphicx}")
print("\\usepackage[left=1cm,right=1cm,top=1cm,bottom=2cm]{geometry}")
print("\\title{Trombinoscope MPSI A}")
print("\\author{HXI DIVINS !!!}")
print("\\date{2020-2021}\n")

print("\\begin{document}")
print("\\maketitle\n")

for i, name in enumerate(liste):
    if i%5 == 0:
        print("\\begin{figure}[!ht]")
    print("    \\begin{subfigure}[b]{0.18\\textwidth}")
    print("    \\captionsetup{justification=centering}")
    print("        \\includegraphics[width=\\textwidth]{" + f"Photo/{name}" + "}")
    nom, prenom = name[:-4].split()
    print("        \\caption*{" + nom + "\\\\" + prenom + "}")
    print("    \\end{subfigure}\\hspace{0.02\\textwidth}%")
    if i%5 == 4:
        print("\\end{figure}")
if i%5 != 4:
    print("\\end{figure}")

print("\\end{document}")


os.system("pdflatex Latex.tex")
