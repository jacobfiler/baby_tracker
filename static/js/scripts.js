document.getElementById('type').addEventListener('change', function () {
    const eventType = this.value;

    // Hide all fields initially
    document.getElementById('feeding_fields').style.display = 'none';
    document.getElementById('sleep_fields').style.display = 'none';
    document.getElementById('diaper_fields').style.display = 'none';

    // Show the relevant fields based on the selected event type
    if (eventType === 'feeding') {
        document.getElementById('feeding_fields').style.display = 'block';
    } else if (eventType === 'sleep') {
        document.getElementById('sleep_fields').style.display = 'block';
    } else if (eventType === 'diaper') {
        document.getElementById('diaper_fields').style.display = 'block';
    }
});

// Trigger the change event to apply the correct visibility on page load
document.getElementById('type').dispatchEvent(new Event('change'));
