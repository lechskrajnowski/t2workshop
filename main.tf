terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=4.1.0"
    }
  }
}
provider "azurerm" {
  features {}
}

terraform {
  backend "azurerm" {
    resource_group_name  = "rg-LechS"
    storage_account_name = "lechs"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}

resource "azurerm_service_plan" {
  name                = "lechs-app-service-plan"
  location            = "westeurope"
  resource_group_name = "rg-LechS"
  os_type             = "Linux"
  sku_name            = "P0v3"
}


resource "azurerm_linux_web_app" {
  name                = "lechs-webapp-workshop"
  location            = "westeurope"
  resource_group_name = "rg-LechS"
  service_plan_id     = azurerm_service_plan.example.id
  site_config {}
}
