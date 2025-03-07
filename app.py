def main():
    print("Welcome to the Security Knowledge Quiz!")
    print("---------------------------------------")
    
    # Ask a security-related question
    print("\nQuestion: What is the most common type of cyber attack?")
    print("a) Phishing")
    print("b) Malware")
    print("c) DDoS")
    print("d) SQL Injection")
    
    # Get user input
    answer = input("\nYour answer (a/b/c/d): ").strip().lower()
    
    # Process the answer
    if answer == 'a':
        print("\nCorrect! Phishing attacks are the most common type of cyber attack.")
        print("These attacks attempt to steal sensitive information by disguising as trustworthy entities.")
    else:
        print("\nIncorrect. The answer is (a) Phishing.")
        print("Phishing attacks are the most common type of cyber attack, where attackers")
        print("attempt to steal sensitive information by disguising as trustworthy entities.")
    
    print("\nQuestion 2: Which of the following is the best password practice?")
    print("a) Use the same password for all accounts to avoid forgetting them")
    print("b) Use complex passwords and store them in a password manager")
    print("c) Change your passwords every day")
    print("d) Write down passwords on sticky notes for easy access")
    
    answer2 = input("\nYour answer (a/b/c/d): ").strip().lower()

    if answer2 == 'b':
        print("\nCorrect! Using a password manager with complex, unique passwords")
        print("is the most secure approach to password management.")
    
    else:
        print("\nIncorrect. The answer is (b) Use complex passwords and store them in a password manager.")
        print("This approach allows you to have strong, unique passwords for each account")
        print("without having to memorize them all.")


    # Ask if the user wants to learn more
    learn_more = input("\nWould you like to learn more about phishing prevention? (yes/no): ").strip().lower()
    
    if learn_more == 'yes' or learn_more == 'y':
        print("\nPhishing Prevention Tips:")
        print("1. Verify the sender's email address")
        print("2. Don't click on suspicious links")
        print("3. Check for spelling and grammar errors")
        print("4. Never share sensitive information via email")
        print("5. Use multi-factor authentication")
    
    print("\nThank you for using the Security Knowledge Quiz!")

if __name__ == "__main__":
    main()