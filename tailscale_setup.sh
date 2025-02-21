#!/bin/bash
echo "Instalando Tailscale..."
curl -fsSL https://tailscale.com/install.sh | sh && sudo tailscale up --authkey=tskey-auth-kmiii3uRMM11CNTRL-7QojupxCME5SXxNkPR11F5BQuFKcc2nQL
echo "Tailscale configurado."
