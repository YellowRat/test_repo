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
           DISPLAY "The square of " UssadaserInput " is " Result
           STOP RUN.
import java.util.Scanner;

public class SquareCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number: ");af
        int userInput = scanner.nextInt();
        
        int result = userInput * userInput;
        
        System.out.println("The square of " + userInput + " is " + result);
        
        scanner.close();
    }
}ewgweg
