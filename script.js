  $(document).ready(function() {
      $('#uploadForm').submit(function(event) {
          event.preventDefault();

          var formData = new FormData($(this)[0]);

          // Make the POST request to the API
          $.ajax({
              url: 'https://1gggivi3t8.execute-api.ap-south-1.amazonaws.com/dev',
              type: 'POST',
              data: formData,
              dataType: 'json',
              processData: false,
              headers: {'content-Type': 'application/pdf'},
              contentType: false,
              success: function(response) {
                console.log(response)
                  $('#message').removeClass('alert-danger').addClass('alert-success').text(response.message);
              },
              error: function(xhr, status, error) {
                  var errorMessage = xhr.responseJSON.error;
                  $('#message').removeClass('alert-success').addClass('alert-danger').text(errorMessage);
              }
          });
      });
  });

  function alertMessage() {
    window.alert("File sucessfully converted to PDF");
}