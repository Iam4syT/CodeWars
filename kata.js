function square_sum(numbers) {
    // Initialize a variable to store the sum of squared numbers
    let sum_of_squares = 0;
    
    // Iterate through the array of numbers
    for (let i = 0; i < numbers.length; i++) {
        // Square each number and add it to the sum
        sum_of_squares += numbers[i] ** 2;
    }
    
    // Return the sum of squared numbers
    return sum_of_squares;
}

for ( i = 1; i <= 3; i++){
    console.log(i)
}
console.log("Go!")