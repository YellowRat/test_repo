       IDENTIFICATION DIVISION.
       PROGRAM-ID. SquareCalculator.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  UserInput      PIC 9(4).
       01  Result         PIC 9(8).

       PROCEDURE DIVISION.
       BEGIN.
           DISPLAY "Enter a number: "
           ACCEPT UserInput
           COMPUTE Result = UserInput * UserInput
           DISPLAY "The square of " UserInput " is " Result
           STOP RUN.
import java.util.Scanner;

public class SquareCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number: ");
        int userInput = scanner.nextInt();
        
        int result = userInput * userInput;
        
        System.out.println("The square of " + userInput + " is " + result);
        
        scanner.close();
    }
}


Robert Aragon	489-36-8350	4929-3813-3266-4295
Ashley Borden	514-14-8905	5370-4638-8881-3020
Thomas Conley	690-05-5315	4916-4811-5814-8111
Susan Davis	421-37-1396	4916-4034-9269-8783
Christopher Diaz	458-02-6124	5299-1561-5689-1938


uidai
aadhar
Aadhar
Aadhaar
AADHAR
