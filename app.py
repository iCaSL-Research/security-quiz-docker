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