This is a script to slightly facilitate working with Arche (Université de Lorraine) for submissions by students in large classes.
Ce script sert à faciliter la notation des rendus sur Arche (Université de Lorraine) par des grandes promotions.

STEP 1: Student data

Prepare an Excel xlsx file where you will store the marks and the student information (see the mock file Marks_TP.xlsx).

It has convenient formatting:
- To have a column verifying if all exercises have been graded for a student in a sheet with marks for each exercise, 
	=IF(COUNTBLANK(B2:K2)=0,"YES","NO")
- To calculate the sum of individual exercise marks in another sheet,
	=SUM('TP3'!B3:K3)
- To color every student for whom you are ready to submit the final mark, refer to the values in this newly created column:
	Formula ='TP3'!$L2="YES", applied to All!$A$2:$D$205
	
STEP 2: Organizing files

Download the folder containing all submissions from Arche. It has individual directories, one per each student. The students were instructed to submit a zip archive with their .c files, one per each exercise.
It is easier to grade each exercise in one bulk, so the function process_new_submission in the script grading.py identifies the student number from the file (you could use the submission ID provided by arche instead), unzips each student's submission, identifies the exercises there and puts, for example, the solution for the exercise 3 into To grade/exo3, prepending the student ID to the original file name.

By adapting the your parameters in the header of grading.py and running the script, you will also get such information as follows:

	Student 33333333 (Pierre Dupont) submitted the following exercises: + + - + + + + + + + (the folder Pierre Dupont_334615636_assignsubmission_file_).
	Student 44444444 (Anais Chretien) submitted the following exercises: + + + + - - - - + + (the folder Anais Chretien_343663099_assignsubmission_file_).
	-----------------------------------------
	Please verify whether the student Mark Zucchiniberg (folder Mark Zuciniberg_351351551_assignsubmission_file_) has the student number 555555555.
	-----------------------------------------
	-----------------------------------------
	File(s) Untitled1 have been found for student 323513511 (Lea Wagner), in the folder Lea Wagner_34451261_assignsubmission_file_.
	-----------------------------------------

If a student did not submit a file for a particular exercise, it is immediately noted in the file that his mark for that exercise is 0.	
	
STEP 3: Grading

Now such folders as To grade/exo3 contain all submissions for this exercise, and you can grade them together. To assign a mark, say, 3.5, just write
	/* Mark 3.5 */
anywhere in the student's file.
If you run process_grades from grading.py now, the script will pick up your mark and put it in the correspondent place of the file with the marks. It will also remove the graded file from the folder, leaving only those files you haven't graded yet.

STEP 4: Handling new submissions

If more students give in their work and now you have a folder where a part of the exercises has been already graded and a part has not, the script is robust and will copy to To grade/ only those files that you have not graded yet, according to the file.
If some student updates his or her submitted file, if you already graded the previous version or the exercise did not use to exist, the script will not be able to know this. It will see the old mark or the zero put for a non-existent exercise and discard the file as a graded one.