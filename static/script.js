document.addEventListener('DOMContentLoaded', () => {
    const encryptForm = document.querySelector('#encrypt-form');
    const encryptBtn = document.querySelector('#encrypt-btn');
    const decryptForm = document.querySelector('#decrypt-form');
    const decryptBtn = document.querySelector('#decrypt-btn');
    const encryptResultDiv = document.querySelector('#encrypt-result');
    const decryptResultDiv = document.querySelector('#decrypt-result');
  
    encryptForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const messageInput = document.querySelector('#message');
      const message = messageInput.value.trim();
  
      if (message !== '') {
        encryptBtn.disabled = true;
        encryptResultDiv.textContent = 'Encrypting...';
  
        fetch('/encrypt', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          body: `message=${encodeURIComponent(message)}`,
        })
          .then((response) => response.json())
          .then((data) => {
            encryptBtn.disabled = false;
            encryptResultDiv.textContent = `Encrypted message: ${data.encrypted}`;
  
            const copyBtn = document.createElement('button');
            copyBtn.className = 'copy-btn';
            copyBtn.innerHTML = '<i class="fas fa-copy"></i>';
            copyBtn.addEventListener('click', () => {
              navigator.clipboard.writeText(data.encrypted)
                .then(() => alert('Message copied!'))
                .catch((error) => console.error('Error copying message:', error));
            });
  
            encryptResultDiv.appendChild(copyBtn);
          })
          .catch((error) => {
            encryptBtn.disabled = false;
            encryptResultDiv.textContent = 'Error occurred while encrypting.';
            console.error(error);
          });
      }
    });
  
    decryptForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const encryptedInput = document.querySelector('#encrypted');
      const encryptedMessage = encryptedInput.value.trim();
  
      if (encryptedMessage !== '') {
        decryptBtn.disabled = true;
        decryptResultDiv.textContent = 'Decrypting...';
  
        fetch('/decrypt', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          body: `encrypted=${encodeURIComponent(encryptedMessage)}`,
        })
          .then((response) => response.json())
          .then((data) => {
            decryptBtn.disabled = false;
            decryptResultDiv.textContent = `Decrypted message: ${data.decrypted}`;
  
            const copyBtn = document.createElement('button');
            copyBtn.className = 'copy-btn';
            copyBtn.innerHTML = '<i class="fas fa-copy"></i>';
            copyBtn.addEventListener('click', () => {
              navigator.clipboard.writeText(data.decrypted)
                .then(() => alert('Message copied!'))
                .catch((error) => console.error('Error copying message:', error));
            });
  
            decryptResultDiv.appendChild(copyBtn);
          })
          .catch((error) => {
            decryptBtn.disabled = false;
            decryptResultDiv.textContent = 'Error occurred while decrypting.';
            console.error(error);
          });
      }
    });
  });
  
  


// document.addEventListener('DOMContentLoaded', () => {
//     const encryptForm = document.querySelector('#encrypt-form');
//     const encryptBtn = document.querySelector('#encrypt-btn');
//     const resultDiv = document.querySelector('#result');
  
//     encryptForm.addEventListener('submit', (e) => {
//       e.preventDefault();
//       const messageInput = document.querySelector('#message');
//       const message = messageInput.value.trim();
  
//       if (message !== '') {
//         encryptBtn.disabled = true;
//         resultDiv.textContent = 'Encrypting...';
  
//         fetch('/encrypt', {
//           method: 'POST',
//           headers: {
//             'Content-Type': 'application/x-www-form-urlencoded',
//           },
//           body: `message=${encodeURIComponent(message)}`,
//         })
//           .then((response) => response.json())
//           .then((data) => {
//             encryptBtn.disabled = false;
//             resultDiv.textContent = `Encrypted message: ${data.encrypted}`;
//           })
//           .catch((error) => {
//             encryptBtn.disabled = false;
//             resultDiv.textContent = 'Error occurred while encrypting.';
//             console.error(error);
//           });
//       }
//     });
//   });
  